# ``WKInternalsNotes/WKBaseScrollView/_updateOverlayRegionsBehavior(_:)``

オーバーレイ領域の挙動を更新する。

## Objective-C Declaration
```objective-c
- (void)_updateOverlayRegionsBehavior:(BOOL)selected;
```

## Discussion
OSS の実装では no-op。内部追加実装が存在する場合はそちらが利用される。

## References
- [`WKBaseScrollView.h#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.h#L70)
- [`WKBaseScrollView.mm#L263`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.mm#L263)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
