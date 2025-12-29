# ``WKInternalsNotes/_WKActivatedElementInfo/_initWithType(_:URL:imageURL:location:title:ID:rect:image:imageMIMEType:isAnimatedImage:isAnimating:canShowAnimationControls:animationsUnderElement:userInfo:)``

アクティブ要素情報をまとめて初期化する内部イニシャライザ。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithType:(_WKActivatedElementType)type URL:(NSURL *)url imageURL:(NSURL *)imageURL location:(const WebCore::IntPoint&)location title:(NSString *)title ID:(NSString *)ID rect:(CGRect)rect image:(WebCore::ShareableBitmap*)image imageMIMEType:(NSString *)imageMIMEType isAnimatedImage:(BOOL)isAnimatedImage isAnimating:(BOOL)isAnimating canShowAnimationControls:(BOOL)canShowAnimationControls animationsUnderElement:(Vector<WebCore::ElementAnimationContext>)animationsUnderElement userInfo:(NSDictionary *)userInfo;
```

## Discussion
URL/画像 URL/タイトル/ID/位置/矩形/画像/MIME などをコピーして保持し、`type` と `isAnimatedImage` を設定する。iOS では `userInfo`、`isAnimating`、`canShowAnimationControls`、`animationsUnderElement` も保存する。

## References
- [`_WKActivatedElementInfoInternal.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfoInternal.h#L42)
- [`_WKActivatedElementInfo.mm#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L109)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
