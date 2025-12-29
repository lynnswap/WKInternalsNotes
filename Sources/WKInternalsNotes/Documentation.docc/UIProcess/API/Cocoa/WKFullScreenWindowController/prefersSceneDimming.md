# ``WKInternalsNotes/WKFullScreenWindowController/prefersSceneDimming``

visionOS でシーン暗転を行うべきかを返す。

## Objective-C Declaration
```objective-c
@property (readonly, assign, nonatomic) BOOL prefersSceneDimming;
```

## Default Value
既定は `NO`。設定や動画状態に応じて `YES` になる。

## Discussion
`fullscreenSceneDimmingEnabled` が無効なら常に `NO`。有効な場合は、要素フルスクリーン中の `bestVideo` があれば `playbackSessionModel()->prefersAutoDimming()` の値を返す。

## References
- [`WKFullScreenWindowControllerIOS.mm#L1977`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1977)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
