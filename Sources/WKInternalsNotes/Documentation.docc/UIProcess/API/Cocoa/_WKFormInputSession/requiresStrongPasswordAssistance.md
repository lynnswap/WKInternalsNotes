# ``WKInternalsNotes/_WKFormInputSession/requiresStrongPasswordAssistance``

強いパスワード補助が必要かを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL requiresStrongPasswordAssistance WK_API_AVAILABLE(ios(12.0));
```

## Default Value
初期化時に渡された値。

## Discussion
初期化時に設定した `_requiresStrongPasswordAssistance` をそのまま返す。

## References
- [`WKContentViewInteraction.mm#L775`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L775)
- [`WKContentViewInteraction.mm#L893`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L893)
- [`_WKFormInputSession.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFormInputSession.h#L46)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
