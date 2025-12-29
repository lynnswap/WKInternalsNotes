# ``WKInternalsNotes/WKFullScreenViewController/_effectiveFullscreenInsets``

フルスクリーン時に適用する実効インセットを計算する。

## Objective-C Declaration
```objective-c
@property (readonly, nonatomic) WebCore::FloatBoxExtent _effectiveFullscreenInsets;
```

## Default Value
`safeAreaInsets` を基に都度計算される。

## Discussion
`safeAreaInsets` から `FloatBoxExtent` を作成し、キャンセルボタンの下端位置に合わせて上側インセットを調整する。

## References
- [`WKFullScreenViewController.mm#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L146)
- [`WKFullScreenViewController.mm#L1005`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L1005)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
