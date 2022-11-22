package com.common.DoYouKnow.dto;

import com.common.DoYouKnow.domain.entity.DYKClub;
import com.common.DoYouKnow.domain.entity.DYKClubContent;
import lombok.*;

import java.util.ArrayList;
import java.util.List;

@NoArgsConstructor
@AllArgsConstructor
@Builder
@Data
public class DYKClubResponse {
    private String name;
    private String imgUrl;
    private List<DYKClubContentResponse> dykClubContentResponses = new ArrayList<>();

    public static DYKClubResponse response(DYKClub dykClub){
        List<DYKClubContentResponse> tmp = new ArrayList<>();
        for(DYKClubContent t:dykClub.getDykClubContents()){
//            System.out.println("t = " + t);
            DYKClubContentResponse dykClubContentResponse =DYKClubContentResponse.response(t);
            tmp.add(dykClubContentResponse);
        }

        return DYKClubResponse.builder().name(dykClub.getName()).dykClubContentResponses(tmp).imgUrl(dykClub.getImgUrl()).build();
    }
}
