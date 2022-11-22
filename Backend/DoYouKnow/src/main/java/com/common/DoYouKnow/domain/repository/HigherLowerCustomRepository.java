package com.common.DoYouKnow.domain.repository;

import com.common.DoYouKnow.dto.HigherLowerResponse;

import java.util.List;

public interface HigherLowerCustomRepository {
    List<HigherLowerResponse> getHigherLower();
}
