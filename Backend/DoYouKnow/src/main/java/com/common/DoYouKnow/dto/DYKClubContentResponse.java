package com.common.DoYouKnow.dto;

import com.common.DoYouKnow.domain.entity.DYKClubContent;
import lombok.*;

@NoArgsConstructor
@AllArgsConstructor
@Builder
@Data
public class DYKClubContentResponse {
    private String type;
    private String content;

    public static DYKClubContentResponse response(DYKClubContent dykClubContent){
      return DYKClubContentResponse.builder().type(dykClubContent.getType()).content(dykClubContent.getContent()).build();
    }
}
