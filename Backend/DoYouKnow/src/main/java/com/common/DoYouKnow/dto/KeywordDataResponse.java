package com.common.DoYouKnow.dto;

import com.common.DoYouKnow.domain.entity.Keyword;
import lombok.*;

@NoArgsConstructor
@AllArgsConstructor
@Builder
@Data
public class KeywordDataResponse {
    private String name;
    private int count;

    public static KeywordDataResponse response(String name, int count) {
        return KeywordDataResponse.builder().name(name).count(count).build();
    }
}
