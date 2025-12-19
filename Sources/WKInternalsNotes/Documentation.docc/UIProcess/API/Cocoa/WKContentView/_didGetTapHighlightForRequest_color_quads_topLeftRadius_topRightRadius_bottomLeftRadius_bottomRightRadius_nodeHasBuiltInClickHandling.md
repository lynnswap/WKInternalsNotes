# ``WKInternalsNotes/WKContentView/_didGetTapHighlightForRequest(_:color:quads:topLeftRadius:topRightRadius:bottomLeftRadius:bottomRightRadius:nodeHasBuiltInClickHandling:)``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
- (void)_didGetTapHighlightForRequest:(WebKit::TapIdentifier)requestID color:(const WebCore::Color&)color quads:(const Vector<WebCore::FloatQuad>&)highlightedQuads topLeftRadius:(const WebCore::IntSize&)topLeftRadius topRightRadius:(const WebCore::IntSize&)topRightRadius bottomLeftRadius:(const WebCore::IntSize&)bottomLeftRadius bottomRightRadius:(const WebCore::IntSize&)bottomRightRadius nodeHasBuiltInClickHandling:(BOOL)nodeHasBuiltInClickHandling;
```

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`WKContentViewInteraction.h#L803`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L803)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
