# ``WKInternalsNotes/WKFormInputSession/initWithContentView(_:focusedElementInfo:requiresStrongPasswordAssistance:)``

入力セッションの初期状態をセットアップする。

## Objective-C Declaration
```objective-c
- (instancetype)initWithContentView:(WKContentView *)view focusedElementInfo:(WKFocusedElementInfo *)elementInfo requiresStrongPasswordAssistance:(BOOL)requiresStrongPasswordAssistance;
```

## Discussion
`WKContentView` を弱参照で保持し、フォーカス要素情報と強力なパスワード補助の要否フラグを保存するだけの初期化を行う。

## References
- [`WKContentViewInteraction.h#L328`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L328)
- [`WKContentViewInteraction.mm#L775`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L775)
- [`WKContentViewInteraction.mm#L780`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L780)
- [`WKContentViewInteraction.mm#L781`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L781)
- [`WKContentViewInteraction.mm#L782`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L782)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
