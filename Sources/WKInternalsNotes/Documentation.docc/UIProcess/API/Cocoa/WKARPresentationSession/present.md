# ``WKInternalsNotes/WKARPresentationSession/present()``

描画結果を表示する。

## Objective-C Declaration
```objective-c
- (void)present;
```

## Discussion
`capturedImage` をカメラレイヤーに設定し、drawable があれば `present` を呼ぶ。最後にバッファを解放する。

## References
- [`WKARPresentationSession.mm#L215`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L215)
- [`WKARPresentationSession.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.h#L57)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
