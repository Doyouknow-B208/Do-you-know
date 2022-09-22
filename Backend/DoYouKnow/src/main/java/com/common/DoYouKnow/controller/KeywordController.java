package com.common.DoYouKnow.controller;

import com.common.DoYouKnow.service.KeywordService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


@RestController
@RequiredArgsConstructor
@RequestMapping("/keyword")
public class KeywordController {
    private final KeywordService keywordService;

    //국가 리스트
    @GetMapping("/nation")
    public ResponseEntity<?> getNations() {
        return ResponseEntity.status(HttpStatus.OK).body(keywordService.getNations());
    }

    //카테고리 리스트
    @GetMapping("/category")
    public ResponseEntity<?> getCategories() {
        return ResponseEntity.status(HttpStatus.OK).body(keywordService.getCategories());
    }

    //국가별 카테고리별 기간별 키워드  0-- 1주일  period 1 1달 , period 2 2달 로 설정
    @GetMapping("/{nation_id}/{category_id}/{period}")
    public ResponseEntity<?> getPeriodKeyword(@PathVariable("nation_id") Long nation_id,
                                              @PathVariable("category_id") Long category_id,
                                              @PathVariable("period") Long period) {
        return ResponseEntity.status(HttpStatus.OK).body(keywordService.getPeriodKeyword(nation_id, category_id, period));
    }

    //국가별 카테고리별 주간키워드 추이
    @GetMapping("/keywordgraph/{keyword}/{nation_id}/{category_id}/{period}")
    public ResponseEntity<?> getWeekGraph(
            @PathVariable("keyword") String keyword,
            @PathVariable("nation_id") Long nation_id,
            @PathVariable("category_id") Long category_id,
            @PathVariable("period") Long period) {
        return ResponseEntity.status(HttpStatus.OK).body(keywordService.getPeriodGraph(keyword,nation_id, category_id, period));
    }

    //국가별 카테고리별 주간 데이터검색량
    @GetMapping("/searchcount/{nation_id}/{category_id}/week")
    public ResponseEntity<?> getWeekCount(@PathVariable("nation_id") Long nation_id,
                                          @PathVariable("category_id") Long category_id) {
        return null;
    }

    //국가별 카테고리별 1달 데이터검색량
    @GetMapping("/searchcount/{nation_id}/{category_id}/oneMonth")
    public ResponseEntity<?> getOneMonthCount(@PathVariable("nation_id") Long nation_id,
                                              @PathVariable("category_id") Long category_id) {
        return null;
    }

    //국가별 카테고리별 3달 데이터검색량
    @GetMapping("/searchcount/{nation_id}/{category_id}/threeMonth")
    public ResponseEntity<?> getThreeMonthCount(@PathVariable("nation_id") Long nation_id,
                                                @PathVariable("category_id") Long category_id) {
        return null;
    }

    //국가별 카테고리별 6달 데이터검색량
    @GetMapping("/searchcount/{nation_id}/{category_id}/sixMonth")
    public ResponseEntity<?> getSixMonthCount(@PathVariable("nation_id") Long nation_id,
                                              @PathVariable("category_id") Long category_id) {
        return null;
    }


    @GetMapping()
    public ResponseEntity<?> getKeywords() {
        return ResponseEntity.status(HttpStatus.OK).body(keywordService.getlist());
    }

}
