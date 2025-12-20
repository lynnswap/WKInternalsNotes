# ``WKInternalsNotes/WKBaseScrollView/overlayRegionAssociatedLayers``

オーバーレイ領域に関連付くレイヤー集合を返す（テスト用）。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=overlayRegionAssociatedLayersForTesting) HashSet<WebCore::PlatformLayerIdentifier>& overlayRegionAssociatedLayers;
```

## Default Value
空の `HashSet`。

## Discussion
テスト用に関連レイヤー数を参照するためのプロパティ。OSS では更新系メソッドが no-op のため、内部追加実装が無い限り空のままになる。

## References
- [`WKBaseScrollView.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.h#L64)
- [`WKBaseScrollView.mm#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.mm#L119)
- [`WKWebViewTestingIOS.mm#L266`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewTestingIOS.mm#L266)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
