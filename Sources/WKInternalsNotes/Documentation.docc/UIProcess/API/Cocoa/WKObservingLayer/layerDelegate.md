# ``WKInternalsNotes/WKObservingLayer/layerDelegate``

レイヤー状態の変化を通知するデリゲート。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id<WKObservingLayerDelegate> layerDelegate;
```

## Default Value
`nil`（未設定）。

## Discussion
`setSeparated:` で `layerSeparatedDidChange:`、`setContents:` で `contents` が `nil` の場合に `layerWasCleared:` を通知する。弱参照のため未設定時は通知しない。

## References
- [`WKSeparatedImageView.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKSeparatedImageView.h#L48)
- [`WKSeparatedImageView.mm#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKSeparatedImageView.mm#L53)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
