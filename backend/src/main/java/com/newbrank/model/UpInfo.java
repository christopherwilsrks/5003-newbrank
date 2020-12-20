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
@TableName("up_info")
public class UpInfo extends Model<UpInfo> {

    private static final long serialVersionUID = 1L;

    @TableId(value = "id", type = IdType.AUTO)
    private Integer id;

    @TableField("uid")
    private Integer uid;

    @TableField("name")
    private String name;

    @TableField("channel")
    private String channel;

    @TableField("sex")
    private String sex;

    @TableField("face")
    private String face;

    @TableField("sign")
    private String sign;

    @TableField("level")
    private Integer level;

    @TableField("birthday")
    private String birthday;

    @TableField("fans_badge")
    private String fansBadge;

    @TableField("official")
    private String official;

    @TableField("vip")
    private String vip;

    @TableField("nameplate")
    private String nameplate;

    @TableField("top_photo")
    private String topPhoto;

    @TableField("live_room")
    private String liveRoom;

    @TableField("following")
    private Integer following;

    @TableField("follower")
    private Integer follower;

    @TableField("video")
    private Integer video;


    @Override
    protected Serializable pkVal() {
        return this.id;
    }

}
