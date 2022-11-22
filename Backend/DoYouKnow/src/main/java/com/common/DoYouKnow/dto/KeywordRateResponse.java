package com.common.DoYouKnow.dto;

import com.common.DoYouKnow.domain.entity.Keyword;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@AllArgsConstructor
@Builder
@Data
public class KeywordRateResponse {
    private Long nationCount;
    private Long nationRate;

    public static KeywordRateResponse response(Long nationCount, Long nationRate) {
        return KeywordRateResponse.builder().nationCount(nationCount).nationRate(nationRate).build();
    }
}
