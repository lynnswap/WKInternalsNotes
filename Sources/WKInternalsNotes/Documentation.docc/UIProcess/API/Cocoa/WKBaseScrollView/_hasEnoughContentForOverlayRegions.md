# ``WKInternalsNotes/WKBaseScrollView/_hasEnoughContentForOverlayRegions()``

オーバーレイ領域の更新に十分なコンテンツがあるかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)_hasEnoughContentForOverlayRegions;
```

## Discussion
OSS の実装では常に `false` を返す（内部追加実装が存在する場合はそちらが優先される）。

## References
- [`WKBaseScrollView.h#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.h#L67)
- [`WKBaseScrollView.mm#L262`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.mm#L262)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
