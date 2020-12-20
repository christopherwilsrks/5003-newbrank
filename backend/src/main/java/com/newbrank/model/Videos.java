package com.newbrank.model;

import com.baomidou.mybatisplus.annotation.TableName;
import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.extension.activerecord.Model;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableField;
import java.io.Serializable;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.experimental.Accessors;

/**
 * <p>
 * 
 * </p>
 *
 * @author christopher
 * @since 2020-11-19
 */
@Data
@EqualsAndHashCode(callSuper = false)
@Accessors(chain = true)
@TableName("videos")
public class Videos extends Model<Videos> {

    private static final long serialVersionUID = 1L;

    @TableId(value = "id", type = IdType.AUTO)
    private Integer id;

    @TableField("uid")
    private Integer uid;

    @TableField("title")
    private String title;

    @TableField("subtitle")
    private String subtitle;

    @TableField("description")
    private String description;

    @TableField("pic")
    private String pic;

    @TableField("author")
    private String author;

    @TableField("mid")
    private Integer mid;

    @TableField("created")
    private Integer created;

    @TableField("length")
    private String length;

    @TableField("aid")
    private String aid;

    @TableField("bvid")
    private String bvid;

    @TableField("play")
    private Integer play;

    @TableField("comment")
    private Integer comment;

    @TableField("video_review")
    private Integer videoReview;

    @TableField("typeid")
    private Integer typeid;

    @TableField("review")
    private Integer review;


    @Override
    protected Serializable pkVal() {
        return this.id;
    }

}
