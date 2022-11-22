package com.common.DoYouKnow.service;

import com.common.DoYouKnow.config.S3Uploader;
import com.common.DoYouKnow.domain.entity.HigherLower;
import com.common.DoYouKnow.domain.repository.*;
import com.common.DoYouKnow.dto.HigherLowerCreateRequest;
import com.common.DoYouKnow.dto.HigherLowerResponse;
import com.common.DoYouKnow.dto.ImgRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.io.IOException;
import java.util.List;

@Service
@RequiredArgsConstructor
public class HigherLowerServiceImpl implements HigherLowerService{

    private final KeywordRepository keywordRepository;
    private final HigherLowerRepository higherLowerRepository;
    private final HigherLowerCustomRepository higherLowerCustomRepository;
    private final S3Uploader s3Uploader;

    @Override
    @Transactional
    public void updateHigherLower() {
        higherLowerRepository.deleteAllInBatch();

        List<HigherLowerCreateRequest> higherLowerCreateRequests = keywordRepository.getHigherLower();
        
        for (HigherLowerCreateRequest higherLowerCreateRequest : higherLowerCreateRequests) {
//            String imgUrl = "https://dyk.s3.ap-northeast-2.amazonaws.com/Game/"+higherLowerCreateRequest.getName()+".jfif";
            String imgUrl = s3Uploader.getPath(higherLowerCreateRequest.getName()+".jfif");
            HigherLower higherLower = HigherLower.create(higherLowerCreateRequest, imgUrl);
            higherLowerRepository.save(higherLower);
        }
    }

    @Override
    @Transactional
    public List<HigherLowerResponse> getHigherLower() {

        return higherLowerCustomRepository.getHigherLower();
//        List<HigherLower> higherLowers = higherLowerRepository.findAll();
//
//        List<HigherLowerResponse> higherLowerResponses = higherLowers.stream().map(h->HigherLowerResponse.response(
//                h.getName(), h.getImgUrl(), h.getCount()
//        )).collect(Collectors.toList());
//
//        Collections.shuffle(higherLowerResponses);
//
//        return higherLowerResponses;
    }

    @Override
    public void createUpload(ImgRequest imgRequest) throws IOException {
        String imgUrl = s3Uploader.upload(imgRequest.getFile(), "Game");
        higherLowerRepository.save(new HigherLower(imgRequest.getName(), imgUrl));
    }
}
