# ``WKInternalsNotes/_WKTextManipulationToken/userInfo``

ユーザー情報の辞書を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSDictionary<NSString *, id> *userInfo;
```

## Default Value
未設定の場合は `nil`。

## Discussion
`setUserInfo:` では同一/同値の場合は更新せず、必要なときだけコピーして保持する。

## References
- [`_WKTextManipulationToken.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationToken.h#L46)
- [`_WKTextManipulationToken.mm#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationToken.mm#L50)
- [`_WKTextManipulationToken.mm#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationToken.mm#L58)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
