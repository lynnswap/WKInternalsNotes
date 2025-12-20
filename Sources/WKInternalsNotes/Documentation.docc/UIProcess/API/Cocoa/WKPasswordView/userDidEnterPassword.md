# ``WKInternalsNotes/WKPasswordView/userDidEnterPassword``

パスワード入力完了時に呼び出されるハンドラを設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) void (^userDidEnterPassword)(NSString *);
```

## Discussion
`UIDocumentPasswordViewDelegate` の `userDidEnterPassword:forPasswordView:` で、このブロックが設定されていれば入力されたパスワードを渡して呼び出す。

## References
- [`WKPasswordView.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.h#L38)
- [`WKPasswordView.mm#L167`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L167)
- [`WKPasswordView.mm#L170`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L170)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
