# ``WKInternalsNotes/WKFullScreenWindowController/updateImageSource()``

QuickLook フルスクリーン画像のソースを更新する。

## Objective-C Declaration
```objective-c
- (void)updateImageSource;
```

## Discussion
`WebFullScreenManagerProxy` が取得できる場合に `prepareQuickLookImageURL` を呼び、取得した URL を `_previewWindowController` の `updateImage` に渡して更新する。

## References
- [`WKFullScreenWindowControllerIOS.mm#L1198`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1198)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
