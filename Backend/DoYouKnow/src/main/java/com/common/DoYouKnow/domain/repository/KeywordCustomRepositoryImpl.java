package com.common.DoYouKnow.domain.repository;

import com.common.DoYouKnow.domain.entity.Keyword;
import com.common.DoYouKnow.domain.entity.QKeyword;
import com.common.DoYouKnow.dto.HigherLowerResponse;
import com.common.DoYouKnow.dto.KeywordDataResponse;
import com.querydsl.core.Tuple;
import com.querydsl.core.types.dsl.NumberExpression;
import com.querydsl.jpa.impl.JPAQueryFactory;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;

@RequiredArgsConstructor
@Repository
public class KeywordCustomRepositoryImpl implements KeywordCustomRepository {

    @PersistenceContext
    EntityManager em;

    public List<KeywordDataResponse> periodKeyword(Date sdate, Date ndate,Long nation_id, Long category_id) {
        JPAQueryFactory jpaQueryFactory = new JPAQueryFactory(em);
        QKeyword k = new QKeyword("k");

        List<Tuple> fetch = jpaQueryFactory
                .select(k.name, k.count.sum())
                .from(k)
                .where(
                        k.date.between(sdate, ndate)
                                .and(k.nation.id.eq(nation_id))
                                .and(k.category.id.eq(category_id))
                )
                .groupBy(k.name)
                .orderBy(k.count.sum().desc())
                .offset(0)
                .limit(20)
                .fetch();

        List<KeywordDataResponse> keywordDataResponseList = fetch.stream().map(
                f->KeywordDataResponse.response(f.get(k.name), f.get(k.count.sum()))
        ).collect(Collectors.toList());


        return keywordDataResponseList;
    }

    @Override
    public List<Keyword> PeriodGraph(Date sdate, Date ndate, Long nation_id, Long category_id, String keyword) {
        JPAQueryFactory jpaQueryFactory = new JPAQueryFactory(em);
        QKeyword k = new QKeyword("k");
        List<Keyword> keywords = jpaQueryFactory
                .selectFrom(k)
                .where(
                        k.date.between(sdate, ndate)
                                .and(k.nation.id.eq(nation_id))
                                .and(k.category.id.eq(category_id))
                                .and(k.name.eq(keyword))
                )
                .orderBy(k.date.asc())
                .fetch();

        return keywords;
    }

    @Override
    public Long SearchCount(Long nation_id, Long category_id) {
        JPAQueryFactory jpaQueryFactory = new JPAQueryFactory(em);
        QKeyword k = new QKeyword("k");

        //nation 전체 , 특정 카테고리만 구하고 싶을때
        if (nation_id==0 && category_id!=0){
            List<Integer> fetch = jpaQueryFactory
                    .select(k.count.sum())
                    .from(k)
                    .where(k.category.id.eq(category_id))
                    .fetch();
            System.out.println("fetch = " + fetch);
        }
        else if(nation_id!=0 && category_id!=0) {
            List<Integer> fetch = jpaQueryFactory
                    .select(k.count.sum())
                    .from(k)
                    .where(k.nation.id.eq(nation_id)
                            .and(k.category.id.eq(category_id)))
                    .fetch();
            System.out.println("fetch = " + fetch);
        }
        else if(nation_id!=0 && category_id==0) {
            List<Integer> fetch = jpaQueryFactory
                    .select(k.count.sum())
                    .from(k)
                    .where(k.nation.id.eq(nation_id))
                    .fetch();
            System.out.println("fetch = " + fetch);
        }
        else{
            List<Integer> fetch = jpaQueryFactory
                    .select(k.count.sum())
                    .from(k)
                    .fetch();
            System.out.println("fetch = " + fetch);
        }

        return null;
    }

//    @Override
//    public List<HigherLowerResponse> getHigherLowerRand() {
//        JPAQueryFactory jpaQueryFactory = new JPAQueryFactory(em);
//        QKeyword k = new QKeyword("k");
//
//        System.out.println("????");
//        List<Tuple> higherLowers = jpaQueryFactory
//                .select(k.name, k.count.sum())
//                .from(k)
//                .groupBy(k.name)
//                .orderBy(NumberExpression.random().asc())
//                .fetch();
//
//        System.out.println("higherLowers = " + higherLowers);
//
//        List<HigherLowerResponse> higherLowerResponses =
//                higherLowers.stream().map(h -> HigherLowerResponse.response(
//                        h.get(k.name), null, h.get(k.count.sum())
//                )).collect(Collectors.toList());
//
//        return higherLowerResponses;
//    }
}
