# ``WKInternalsNotes/_WKActivatedElementInfo/_initWithType(_:URL:imageURL:location:title:ID:rect:image:imageMIMEType:isAnimatedImage:isAnimating:canShowAnimationControls:animationsUnderElement:userInfo:)``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithType:(_WKActivatedElementType)type URL:(NSURL *)url imageURL:(NSURL *)imageURL location:(const WebCore::IntPoint&)location title:(NSString *)title ID:(NSString *)ID rect:(CGRect)rect image:(WebCore::ShareableBitmap*)image imageMIMEType:(NSString *)imageMIMEType isAnimatedImage:(BOOL)isAnimatedImage isAnimating:(BOOL)isAnimating canShowAnimationControls:(BOOL)canShowAnimationControls animationsUnderElement:(Vector<WebCore::ElementAnimationContext>)animationsUnderElement userInfo:(NSDictionary *)userInfo;
```

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`_WKActivatedElementInfoInternal.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfoInternal.h#L42)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
