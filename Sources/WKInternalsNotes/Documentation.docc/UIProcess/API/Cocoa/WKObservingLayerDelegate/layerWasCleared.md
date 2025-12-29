# ``WKInternalsNotes/WKObservingLayerDelegate/layerWasCleared(_:)``

レイヤーの `contents` がクリアされたときに呼ばれる。

## Objective-C Declaration
```objective-c
- (void)layerWasCleared:(CALayer *)layer;
```

## Discussion
`WKObservingLayer` が `setContents:` を受け取り、`contents` が `nil` の場合に `layerDelegate` へ通知する。

## References
- [`WKSeparatedImageView.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKSeparatedImageView.h#L34)
- [`WKSeparatedImageView.mm#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKSeparatedImageView.mm#L57)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
