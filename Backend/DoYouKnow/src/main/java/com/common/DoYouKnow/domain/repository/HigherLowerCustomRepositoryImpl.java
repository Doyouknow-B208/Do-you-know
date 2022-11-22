package com.common.DoYouKnow.domain.repository;

import com.common.DoYouKnow.domain.entity.QHigherLower;
import com.common.DoYouKnow.domain.entity.QKeyword;;
import com.common.DoYouKnow.dto.HigherLowerResponse;
import com.querydsl.core.Tuple;
import com.querydsl.jpa.impl.JPAQueryFactory;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

@RequiredArgsConstructor
@Repository
public class HigherLowerCustomRepositoryImpl implements HigherLowerCustomRepository {

    @PersistenceContext
    EntityManager em;

    @Value("${cloud.aws.s3.path}")
    String S3Url;

    @Override
    public List<HigherLowerResponse> getHigherLower() {
        JPAQueryFactory jpaQueryFactory = new JPAQueryFactory(em);
        QHigherLower k = new QHigherLower("k");
        QKeyword i = new QKeyword("i");

        List<Tuple> fetch = jpaQueryFactory
                .select(k.name, k.imgUrl, i.count.sum())
                .from(k)
                .innerJoin(i)
                .on(i.name.eq(k.name))
                .groupBy(i.name)
                .fetch();

        List<HigherLowerResponse> higherLowerResponseList = fetch.stream().map(
                h ->HigherLowerResponse.response(
                        h.get(k.name), S3Url+h.get(k.imgUrl), h.get(i.count.sum())
        )).collect(Collectors.toList());

        Collections.shuffle(higherLowerResponseList);
        return higherLowerResponseList;
    }
}
