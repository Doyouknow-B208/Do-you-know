package com.common.DoYouKnow.service;

import com.common.DoYouKnow.dto.*;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import java.util.List;

public interface KeywordService {
    List<KeywordResponse> getlist();

    //국가 리스트
    List<NationResponse> getNations();

    //카테고리 리스트
    List<CategoryResponse> getCategories();

    //국가별 카테고리별 기간 Month로 설정
    List<KeywordDataResponse> getPeriodKeyword(Long nation_id, Long category_id, Long period);

    List<KeywordResponse> getPeriodGraph(String keyword,Long nation_id,Long category_id,Long period);

    Long getWeekCount(Long nation_id,Long category_id);
    KeywordRateResponse getTotalCount(Long nation_id);
//    //국가별 카테고리별 3달 데이터검색량
//    public ResponseEntity<?> getThreeMonthCount(Long nation_id,Long category_id);
//
//    //국가별 카테고리별 6달 데이터검색량
//    public ResponseEntity<?> getSixMonthCount(Long nation_id,Long category_id);
}
