package com.common.DoYouKnow.dto;

import com.common.DoYouKnow.domain.entity.Nation;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@AllArgsConstructor
@Builder
@Data
public class NationResponse {
    private Long id;
    private String name;
    private String code;
    private String language;
    private String twitter_code;

    public static NationResponse response(Nation nation){
        return NationResponse.builder()
                .id(nation.getId())
                .name(nation.getName())
                .code(nation.getCode())
                .language(nation.getLanguage())
                .twitter_code(nation.getTwitter_code())
                .build();
    }

}
