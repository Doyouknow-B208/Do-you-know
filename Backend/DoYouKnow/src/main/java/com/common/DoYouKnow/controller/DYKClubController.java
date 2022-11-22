package com.common.DoYouKnow.controller;

import com.common.DoYouKnow.service.DYKClubService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
@Api(tags = "두유노클럽")
@RequestMapping("/dykclub")
public class DYKClubController {
    private final DYKClubService dykClubService;
    
    @ApiOperation(value = "키워드 리스트")
    @GetMapping("/{category_id}")
    public ResponseEntity<?> getPeriodKeyword(@PathVariable("category_id") Long category_id)
    {
        return ResponseEntity.status(HttpStatus.OK).body(dykClubService.getDYKClubs(category_id));
    }

    @ApiOperation(value = "name에 관련된 키워드")
    @GetMapping("/keyword/{name}")
    public ResponseEntity<?> getPeriodKeyword(@PathVariable("name") String name)
    {
        return ResponseEntity.status(HttpStatus.OK).body(dykClubService.getTwitter(name));
    }
}
