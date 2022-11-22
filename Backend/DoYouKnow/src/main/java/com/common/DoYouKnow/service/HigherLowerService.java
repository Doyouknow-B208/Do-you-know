package com.common.DoYouKnow.service;

import com.common.DoYouKnow.dto.HigherLowerResponse;
import com.common.DoYouKnow.dto.ImgRequest;

import java.io.IOException;
import java.util.List;


public interface HigherLowerService {
    void updateHigherLower();
    List<HigherLowerResponse> getHigherLower();
    void createUpload(ImgRequest imgRequest) throws IOException;
}
