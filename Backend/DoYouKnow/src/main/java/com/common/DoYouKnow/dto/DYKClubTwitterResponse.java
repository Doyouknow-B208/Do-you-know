package com.common.DoYouKnow.dto;

import com.common.DoYouKnow.domain.entity.DYKClubContent;
import com.common.DoYouKnow.domain.entity.DYKClubTwitter;
import lombok.*;

@NoArgsConstructor
@AllArgsConstructor
@Builder
@Data
@ToString
public class DYKClubTwitterResponse {
    private String content;
    public static DYKClubTwitterResponse response(DYKClubTwitter dykClubContent){
        return DYKClubTwitterResponse.builder().content(dykClubContent.getContent()).build();
    }
}
