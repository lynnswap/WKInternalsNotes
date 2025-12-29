# ``WKInternalsNotes/WKFullScreenWindowController/didExitVideoFullscreen()``

visionOS で動画フルスクリーン終了時にステージの暗さを自動調光設定へ合わせる。

## Objective-C Declaration
```objective-c
- (void)didExitVideoFullscreen;
```

## Discussion
`PLATFORM(VISION)` かつ空間フルスクリーン遷移中のみ有効。`bestVideoForElementFullscreen()` の `prefersAutoDimming()` を読み取り、`preferredDarkness` を `Dark` または `Unspecified` に設定する。

## References
- [`WKFullScreenWindowControllerIOS.mm#L1000`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1000)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
