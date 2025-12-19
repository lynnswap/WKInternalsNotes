# ``WKInternalsNotes/WKContentView/_didCommitLayerTree(_:)``

レイヤーツリーのコミット処理を反映する。

## Objective-C Declaration
```objective-c
- (void)_didCommitLayerTree:(const WebKit::RemoteLayerTreeTransaction&)layerTreeTransaction;
```

## Discussion
トランザクションからコンテンツ境界を算出して必要なら `bounds` を更新し、`WKWebView` にコミットを通知する。インタラクションビューの座標更新や固定位置の再計算を行い、条件が揃えば選択状態の更新も行う。

## References
- [`WKContentView.h#L128`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L128)
- [`WKContentView.mm#L1000`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L1000)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
