# ``WKInternalsNotes/WKBaseScrollView/_updateOverlayRegionRects(_:whileStable:)``

オーバーレイ領域の矩形を更新する。

## Objective-C Declaration
```objective-c
- (void)_updateOverlayRegionRects:(const HashSet<WebCore::IntRect>&)overlayRegions whileStable:(BOOL)stable;
```

## Discussion
OSS の実装では no-op。内部追加実装が存在する場合はそちらが利用される。

## References
- [`WKBaseScrollView.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.h#L68)
- [`WKBaseScrollView.mm#L264`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.mm#L264)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
