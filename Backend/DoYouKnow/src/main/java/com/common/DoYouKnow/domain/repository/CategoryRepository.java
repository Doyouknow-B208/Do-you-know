package com.common.DoYouKnow.domain.repository;

import com.common.DoYouKnow.domain.entity.Category;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CategoryRepository extends JpaRepository<Category, Long> {
}