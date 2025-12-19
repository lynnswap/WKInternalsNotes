# ``WKInternalsNotes/WKContentView/_didGetTapHighlightForRequest(_:color:quads:topLeftRadius:topRightRadius:bottomLeftRadius:bottomRightRadius:nodeHasBuiltInClickHandling:)``

タップハイライト情報を受け取って表示を更新する。

## Objective-C Declaration
```objective-c
- (void)_didGetTapHighlightForRequest:(WebKit::TapIdentifier)requestID color:(const WebCore::Color&)color quads:(const Vector<WebCore::FloatQuad>&)highlightedQuads topLeftRadius:(const WebCore::IntSize&)topLeftRadius topRightRadius:(const WebCore::IntSize&)topRightRadius bottomLeftRadius:(const WebCore::IntSize&)bottomLeftRadius bottomRightRadius:(const WebCore::IntSize&)bottomRightRadius nodeHasBuiltInClickHandling:(BOOL)nodeHasBuiltInClickHandling;
```

## Discussion
リクエストIDの整合性やフォーカス要素を確認した上で、ハイライト矩形や色を保存する。ポテンシャルタップ中はフラグを立て、通常時はハイライト表示を行う。

## References
- [`WKContentViewInteraction.h#L803`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L803)
- [`WKContentViewInteraction.mm#L2660`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2660)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
