package com.common.DoYouKnow.controller;

import com.common.DoYouKnow.dto.KeywordRateResponse;
import com.common.DoYouKnow.dto.KeywordResponse;
import com.common.DoYouKnow.service.KeywordService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
@RequiredArgsConstructor
@Api(tags = "데이터랩")
@RequestMapping("/keyword")
public class KeywordController {
    private final KeywordService keywordService;

    //국가 리스트
    @ApiOperation(value = "국가 리스트")
    @GetMapping("/nation")
    public ResponseEntity<?> getNations() {
        return ResponseEntity.status(HttpStatus.OK).body(keywordService.getNations());
    }

    //카테고리 리스트
    @ApiOperation(value = "카테고리 리스트")
    @GetMapping("/category")
    public ResponseEntity<?> getCategories() {
        return ResponseEntity.status(HttpStatus.OK).body(keywordService.getCategories());
    }

    //국가별 카테고리별 기간별 키워드  0-- 1주일  period 1 1달 , period 2 2달 로 설정
    @ApiOperation(value = "/국가별 카테고리별 기간별 키워드")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "nation_id", value = "나라 ID", required = true, dataType = "long")
            ,@ApiImplicitParam(name = "category_id", value = "카테고리 ID", required = true, dataType = "long")
            , @ApiImplicitParam(name = "period", value = "기간 (0:1주일, 1:1달, 2:2달)", required = true, dataType = "long")
    })
    @GetMapping("/{nation_id}/{category_id}/{period}")
    public ResponseEntity<?> getPeriodKeyword(@PathVariable("nation_id") Long nation_id,
                                              @PathVariable("category_id") Long category_id,
                                              @PathVariable("period") Long period) {
        return ResponseEntity.status(HttpStatus.OK).body(keywordService.getPeriodKeyword(nation_id, category_id, period));
    }

    //국가별 카테고리별 주간키워드 추이
    @ApiOperation(value = "국가별 카테고리별 주간키워드 추이")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "keyword", value = "키워드", required = true, dataType = "string")
            ,@ApiImplicitParam(name = "nation_id", value = "나라 ID", required = true, dataType = "long")
            ,@ApiImplicitParam(name = "category_id", value = "카테고리 ID", required = true, dataType = "long")
            ,@ApiImplicitParam(name = "period", value = "기간 (0:1주일, 1:1달, 2:2달)", required = true, dataType = "long")
    })
    @GetMapping("/keywordgraph/{keyword}/{nation_id}/{category_id}/{period}")
    public ResponseEntity<?> getWeekGraph(
            @PathVariable("keyword") String keyword,
            @PathVariable("nation_id") Long nation_id,
            @PathVariable("category_id") Long category_id,
            @PathVariable("period") Long period) {
        List<KeywordResponse> periodGraph = keywordService.getPeriodGraph(keyword, nation_id, category_id, period);
        for (KeywordResponse keywordResponse : periodGraph) {
            System.out.println("keywordResponse.getDate() = " + keywordResponse.getDate());
        }
        return ResponseEntity.status(HttpStatus.OK).body(keywordService.getPeriodGraph(keyword,nation_id, category_id, period));
    }

    //국가별 카테고리별 주간 데이터검색량
    @ApiOperation(value = "국가별 카테고리별 주간 데이터검색량")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "nation_id", value = "나라 ID", required = true, dataType = "long")
            ,@ApiImplicitParam(name = "category_id", value = "카테고리 ID", required = true, dataType = "long")
    })
    @GetMapping("/searchcount/{nation_id}/{category_id}")
    public ResponseEntity<?> getWeekCount(@PathVariable("nation_id") Long nation_id,
                                          @PathVariable("category_id") Long category_id) {
        return ResponseEntity.status(HttpStatus.OK).body(keywordService.getWeekCount(nation_id,category_id));
    }

    //국가별 총 데이터검색량과 비율
    @ApiOperation(value = "국가별 총 데이터검색량과 비율")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "nation_id", value = "나라 ID", required = true, dataType = "long")
    })
    @GetMapping("/searchcount/{nation_id}")
    public ResponseEntity<?> getTotalCount(@PathVariable("nation_id") Long nation_id) {
        return ResponseEntity.status(HttpStatus.OK).body(keywordService.getTotalCount(nation_id));
    }


//    @GetMapping()
//    public ResponseEntity<?> getKeywords() {
//        return ResponseEntity.status(HttpStatus.OK).body(keywordService.getlist());
//    }

}
