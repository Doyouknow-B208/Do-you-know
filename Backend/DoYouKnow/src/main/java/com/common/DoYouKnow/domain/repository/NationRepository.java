package com.common.DoYouKnow.domain.repository;

import com.common.DoYouKnow.domain.entity.Nation;
import org.springframework.data.jpa.repository.JpaRepository;

public interface NationRepository extends JpaRepository<Nation, Long> {
}