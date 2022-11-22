package com.common.DoYouKnow.domain.repository;

import com.common.DoYouKnow.domain.entity.Category;
import com.common.DoYouKnow.domain.entity.DYKClub;
import org.springframework.data.jpa.repository.JpaRepository;

public interface DYKClubRepository extends JpaRepository<DYKClub, Long> {
}