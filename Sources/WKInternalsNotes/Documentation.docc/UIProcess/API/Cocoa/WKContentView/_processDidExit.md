# ``WKInternalsNotes/WKContentView/_processDidExit()``

Webプロセス終了時の後処理を行う。

## Objective-C Declaration
```objective-c
- (void)_processDidExit;
```

## Discussion
アクセシビリティ登録の解除、インタラクションのクリーンアップ、インスペクタ表示の解除、可視性伝播ビューの除去、印刷状態のリセットを行う。

## References
- [`WKContentView.h#L98`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L98)
- [`WKContentView.mm#L900`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L900)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
