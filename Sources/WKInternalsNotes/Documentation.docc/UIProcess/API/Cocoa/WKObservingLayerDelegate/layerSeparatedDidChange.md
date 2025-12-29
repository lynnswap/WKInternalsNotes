# ``WKInternalsNotes/WKObservingLayerDelegate/layerSeparatedDidChange(_:)``

レイヤーの分離状態が変化したときに呼ばれる。

## Objective-C Declaration
```objective-c
- (void)layerSeparatedDidChange:(CALayer *)layer;
```

## Discussion
`WKObservingLayer` の `setSeparated:` で分離状態が更新されるたびに、`layerDelegate` へ通知する。

## References
- [`WKSeparatedImageView.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKSeparatedImageView.h#L33)
- [`WKSeparatedImageView.mm#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKSeparatedImageView.mm#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
