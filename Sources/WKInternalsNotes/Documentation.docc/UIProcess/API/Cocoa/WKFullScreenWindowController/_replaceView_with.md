# ``WKInternalsNotes/WKFullScreenWindowController/_replaceView(_:with:)``

指定したビューを同じ階層の別ビューに置換し、フレームとリサイズ挙動を引き継ぐ。

## Objective-C Declaration
```objective-c
- (void)_replaceView:(NSView *)view with:(NSView *)otherView;
```

## Discussion
`CATransaction` でアクションを無効化し、`otherView` に `view` の `frame` と `autoresizingMask` をコピーしたうえで、`view` の superview に `otherView` を挿し替える。アニメーションを発生させず、`view` を除去するため、フルスクリーン用のプレースホルダーと WebView の差し替えに使える。

## References
- [`WKFullScreenWindowController.mm#L937`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L937)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
