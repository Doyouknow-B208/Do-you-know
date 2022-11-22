package com.common.DoYouKnow.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@AllArgsConstructor
@Builder
@Data
public class HigherLowerResponse {
    private String name;
    private String imgUrl;
    private int count;

    public static HigherLowerResponse response(String name, String imgUrl, int count){
        return HigherLowerResponse.builder()
                .name(name)
                .imgUrl(imgUrl)
                .count(count)
                .build();
    }
}
