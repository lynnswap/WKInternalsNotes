# ``WKInternalsNotes/WKBaseScrollView/overlayRegionRects``

オーバーレイ領域の矩形セットを返す（テスト用）。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=overlayRegionsForTesting) HashSet<WebCore::IntRect>& overlayRegionRects;
```

## Default Value
空の `HashSet`。

## Discussion
テスト用にオーバーレイ領域を参照するためのプロパティ。OSS では更新系メソッドが no-op のため、内部追加実装が無い限り空のままになる。

## References
- [`WKBaseScrollView.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.h#L63)
- [`WKBaseScrollView.mm#L118`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.mm#L118)
- [`WKWebViewTestingIOS.mm#L257`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewTestingIOS.mm#L257)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
