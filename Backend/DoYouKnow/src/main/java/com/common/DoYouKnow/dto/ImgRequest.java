package com.common.DoYouKnow.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import org.springframework.web.multipart.MultipartFile;

@Builder
@Getter
@Setter
public class ImgRequest {
    String name;
    MultipartFile file;
}
