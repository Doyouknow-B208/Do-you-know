package com.common.DoYouKnow.domain.repository;

import com.common.DoYouKnow.domain.entity.*;
import com.common.DoYouKnow.dto.DYKClubResponse;
import com.common.DoYouKnow.dto.DYKClubTwitterResponse;
import com.querydsl.jpa.impl.JPAQueryFactory;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import java.util.ArrayList;
import java.util.List;

@RequiredArgsConstructor
@Repository
public class DYKClubCustomRepositoryImpl implements DYKClubCustomRepository {
    @PersistenceContext
    EntityManager em;
    @Override
    public List<DYKClubResponse> getDYKClublist(Long category_id) {
        JPAQueryFactory jpaQueryFactory = new JPAQueryFactory(em);
        QDYKClub k = new QDYKClub("k");

        List<DYKClub> dykClubs = jpaQueryFactory
                .selectFrom(k)
                .where(k.category.id.eq(category_id))
                .limit(3)
                .fetch();

        List<DYKClubResponse> dykClubResponses = new ArrayList<>();
        for (DYKClub tmp: dykClubs){
            dykClubResponses.add(DYKClubResponse.response(tmp));
        }

        return dykClubResponses;
    }

    @Override
    public List<DYKClubTwitterResponse> getTwitterlist(String name) {
        JPAQueryFactory jpaQueryFactory = new JPAQueryFactory(em);
        QDYKClubTwitter t = new QDYKClubTwitter("t");
        List<DYKClubTwitter> dykClubTwitters = jpaQueryFactory
                .selectFrom(t)
                .where(t.dykClub.name.eq(name))
                .limit(10)
                .fetch();
        List<DYKClubTwitterResponse> dykClubTwitterResponses = new ArrayList<>();
        for (DYKClubTwitter tmp: dykClubTwitters){
            dykClubTwitterResponses.add(DYKClubTwitterResponse.response(tmp));
        }
        return dykClubTwitterResponses;
    }
}
