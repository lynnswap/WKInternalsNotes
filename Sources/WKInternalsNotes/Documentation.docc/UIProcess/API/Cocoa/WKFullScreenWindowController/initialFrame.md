# ``WKInternalsNotes/WKFullScreenWindowController/initialFrame``

フルスクリーン遷移の開始フレーム（画面座標）を保持する。

## Objective-C Declaration
```objective-c
@property (readonly) NSRect initialFrame;
```

## Default Value
初期値は `NSZeroRect`。`beganEnterFullScreenWithInitialFrame:finalFrame:` で設定される。

## Discussion
`initialFrame` は `_initialFrame` に束縛され、遷移アニメーションや退出時の位置計算に使われる。

## References
- [`WKFullScreenWindowController.mm#L292`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L292)
- [`WKFullScreenWindowController.mm#L466`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L466)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
