# ``WKInternalsNotes/_WKContentWorldConfiguration/allowElementUserInfo``

要素への userInfo 付与を許可するかを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL allowElementUserInfo;
```

## Default Value
`NO`。

## Discussion
`WKContentWorld` 生成時に `AllowElementUserInfo` オプションへ反映され、既存の world と値が一致しない場合は例外になる。

## References
- [`WKContentWorld.mm#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentWorld.mm#L32)
- [`WKContentWorld.mm#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentWorld.mm#L101)
- [`WKContentWorldConfiguration.mm#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentWorldConfiguration.mm#L54)
- [`_WKContentWorldConfiguration.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContentWorldConfiguration.h#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
