# ``WKInternalsNotes/WKPasswordView/initWithFrame(_:documentName:)``

ドキュメント用パスワード入力ビューを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithFrame:(CGRect)frame documentName:(NSString *)documentName;
```

## Discussion
`documentName` をコピーして保持し、`UIDocumentPasswordView` を生成する。生成したパスワードビューを `bounds` でレイアウトし、delegate と autoresizing を設定して自身のサブビューに追加する。

## References
- [`WKPasswordView.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.h#L32)
- [`WKPasswordView.mm#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L55)
- [`WKPasswordView.mm#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L61)
- [`WKPasswordView.mm#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L62)
- [`WKPasswordView.mm#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L67)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
