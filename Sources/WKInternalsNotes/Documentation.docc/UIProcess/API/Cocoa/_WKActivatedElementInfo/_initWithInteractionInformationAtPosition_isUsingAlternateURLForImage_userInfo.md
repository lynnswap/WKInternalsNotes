# ``WKInternalsNotes/_WKActivatedElementInfo/_initWithInteractionInformationAtPosition(_:isUsingAlternateURLForImage:userInfo:)``

位置情報から `_WKActivatedElementInfo` を構築する内部イニシャライザ。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithInteractionInformationAtPosition:(const WebKit::InteractionInformationAtPosition&)information isUsingAlternateURLForImage:(BOOL)isUsingAlternateURLForImage userInfo:(NSDictionary *)userInfo;
```

## Discussion
`information` から URL/画像 URL/タイトル/矩形/ID/画像/MIME などを取り出し、要素種別をリンク/画像/添付/未指定で設定する。アニメーション関連フラグや `isUsingAlternateURLForImage`、`userInfo` も保存する。

## References
- [`_WKActivatedElementInfoInternal.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfoInternal.h#L41)
- [`_WKActivatedElementInfo.mm#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L55)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
