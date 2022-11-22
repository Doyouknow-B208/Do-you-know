package com.common.DoYouKnow.domain.entity;

import com.common.DoYouKnow.dto.HigherLowerCreateRequest;
import lombok.*;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Builder
public class HigherLower {
    @Id
    private String name;
    private String imgUrl;

    public HigherLower(String name, String imgUrl) {
        this.name = name;
        this.imgUrl = imgUrl;
    }

    public static HigherLower create(HigherLowerCreateRequest higherLowerCreateRequest, String imgUrl){
        HigherLower higherLower = new HigherLower();
        higherLower.name = higherLowerCreateRequest.getName();
        higherLower.imgUrl = imgUrl;
//        higherLower.count = higherLowerCreateRequest.getCount();

        return higherLower;
    }
}
