package com.common.DoYouKnow.controller;

import com.common.DoYouKnow.dto.ImgRequest;
import com.common.DoYouKnow.service.HigherLowerService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

@RestController
@RequiredArgsConstructor
@Api(tags = "더많이더적게")
@RequestMapping("/higherlower")
public class HigherLowerController {

    private final HigherLowerService higherLowerService;

//    @ApiOperation(value = "더많이더적게 최신날짜 업데이트")
//    @PostMapping()
//    public ResponseEntity<?> updateHigherLower(){
//        higherLowerService.updateHigherLower();
//        return ResponseEntity.status(HttpStatus.OK).body("update dataset");
//    }

    @ApiOperation(value = "관리자용 이미지 업로드")
    @PostMapping()
    public ResponseEntity<?> updateHigherLower(@ModelAttribute ImgRequest imgRequest){
        try {
            higherLowerService.createUpload(imgRequest);
            return ResponseEntity.status(HttpStatus.OK).body("img upload success");
        } catch (IOException e) {
            return ResponseEntity.status(HttpStatus.OK).body("img upload failed");
        }
    }

    @ApiOperation(value = "더많이더적게 랜덤으로 가져오기")
    @GetMapping()
    public ResponseEntity<?> getHigherLower(){
        return ResponseEntity.status(HttpStatus.OK).body(higherLowerService.getHigherLower());
    }
}
