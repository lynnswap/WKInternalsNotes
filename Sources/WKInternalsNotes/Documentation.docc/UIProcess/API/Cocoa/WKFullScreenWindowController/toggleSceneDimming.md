# ``WKInternalsNotes/WKFullScreenWindowController/toggleSceneDimming()``

visionOS のシーン暗転設定をトグルし、必要ならステージ暗さを更新する。

## Objective-C Declaration
```objective-c
- (void)toggleSceneDimming;
```

## Discussion
`prefersSceneDimming` を反転した値を `playbackSessionModel()->setPrefersAutoDimming` に設定する。フルスクリーン中であれば `MRUIStage` の `preferredDarkness` を更新し、暗転の有無を反映する。

## References
- [`WKFullScreenWindowControllerIOS.mm#L2181`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L2181)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
