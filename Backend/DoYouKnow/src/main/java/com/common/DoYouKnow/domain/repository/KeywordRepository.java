package com.common.DoYouKnow.domain.repository;

import com.common.DoYouKnow.domain.entity.HigherLower;
import com.common.DoYouKnow.domain.entity.Keyword;
import com.common.DoYouKnow.dto.HigherLowerCreateRequest;
import com.common.DoYouKnow.dto.HigherLowerResponse;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;

public interface KeywordRepository extends JpaRepository<Keyword,Long> {
    @Query(value = "select new com.common.DoYouKnow.dto.HigherLowerCreateRequest(k.name, sum(k.count)) from Keyword k group by k.name")
    List<HigherLowerCreateRequest> getHigherLower();

    @Query(value = "select count(k.name) from Keyword k where k.nation.id = :nation_id")
    Long NationLength(@Param("nation_id")Long nation_id);

}
